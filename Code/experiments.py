import model
import pandas as pd
import data_bank
import prompt_bank

def task_with_concise_CoT(cluases: pd.DataFrame, model: model.Model, model_name: str):
    
    CoT_style = 'concise_cot'
    
    # Prepare files for the output 
    result_filename = f'../Result/{CoT_style}_{model_name}.csv'
    if not data_bank.is_file_exits(result_filename):
        # Prepareing to save the results
        fields = ['text','ground_truth','model_prediction','model_Justification','Human_AI_Alignment']
        data_bank.open_result_file(filename= result_filename, fields= fields)
    
    for i in cluases.itertuples(index=True):
       
              
        clause_text = i.text
        clause_grond_truth = i.answer
        ith_result=[clause_text,clause_grond_truth] 
          
        prompt = prompt_bank.qurey_prompt('concise_cot_prompt',clause_text)
        # print('prompt: ', prompt)
        
        model_output = model.qurey_LLM_model(user_prompt=prompt)
        print('model_output: ', model_output)
        model_output_processed = data_bank.josn_processing(model_output)
        # print('model_output_processed: ', model_output_processed)

        ith_result.append(model_output_processed['final_decision'])
        ith_result.append(model_output_processed['justification'])
        
        if clause_grond_truth == model_output_processed['final_decision']:
            ith_result.append(1)
        else:
            ith_result.append(0)
       
        data_bank.save_result(result_filename,ith_result)
        
    
def task_with_structured_CoT(cluases: pd.DataFrame, model: model.Model, model_name: str):
    
    CoT_style = 'structured_cot'
    
    # Prepare files for the output 
    result_filename = f'../Result/{CoT_style}_{model_name}.csv'
    if not data_bank.is_file_exits(result_filename):
        # Prepareing to save the results
        fields = ['text','ground_truth','model_legal_principle','model_power_imbalance','model_consumer_harm','model_prediction','Human_AI_Alignment']
        data_bank.open_result_file(filename= result_filename, fields= fields)
    
    for i in cluases.itertuples(index=True):
       
        clause_text = i.text
        clause_grond_truth = i.answer
        ith_result=[clause_text,clause_grond_truth] 
          
        prompt = prompt_bank.qurey_prompt('structured_cot_prompt',clause_text)
        print('prompt: ', prompt)
        model_output = model.qurey_LLM_model(user_prompt=prompt)
        print('model_output: ', model_output)
        model_output_processed = data_bank.josn_processing(model_output)
        print('model_output_processed: ', model_output_processed)

        ith_result.append(model_output_processed['legal_principle'])
        ith_result.append(model_output_processed['power_imbalance'])
        ith_result.append(model_output_processed['consumer_harm'])
        ith_result.append(model_output_processed['final_decision'])
        if clause_grond_truth == model_output_processed['final_decision']:
            ith_result.append(1)
        else:
            ith_result.append(0)
       
        data_bank.save_result(result_filename,ith_result)
        
