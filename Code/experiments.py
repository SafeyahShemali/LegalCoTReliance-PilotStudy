import model
import pandas as pd
import data_bank
import prompt_bank

def task_with_concise_CoT(cluases: pd.DataFrame, model: model.Model, model_name: str):
    
    CoT_style = 'concise_cot'
    # tracking the accuracy of the model
    Correct_AI = 0
    Incorrect_AI = 0
    
    # Prepare files for the output 
    result_filename = f'Result/{CoT_style}_{model_name}.csv'
    if not data_bank.is_file_exits(result_filename):
        # Prepareing to save the results
        fields = ['text','ground_truth','sample_index','model_Justification','model_prediction','Human_AI_Alignment']
        data_bank.open_result_file(filename= result_filename, fields= fields)
    
    for i in cluases.itertuples(index=True):
       
        clause_text = i.text
        clause_answer = i.answer
        cluase_index = i.index
        ith_result=[clause_text,clause_answer,cluase_index] 
          
        prompt = prompt_bank.qurey_prompt('concise_cot_prompt',clause_text)
        print('prompt:\n', prompt, '\n-------------\n')
        
        model_output = model.qurey_LLM_model(user_prompt=prompt)
        model_output_processed = data_bank.josn_processing(model_output)

        ith_result.append(model_output_processed['justification'])
        ith_result.append(model_output_processed['final_decision'])

        if clause_answer == model_output_processed['final_decision']:
            ith_result.append(1)
            Correct_AI = +1
        else:
            ith_result.append(0)
            Incorrect_AI = +1
       
        data_bank.save_result(result_filename,ith_result)
        
    return Correct_AI, Incorrect_AI
        
    
def task_with_structured_CoT(cluases: pd.DataFrame, model: model.Model, model_name: str):
    
    CoT_style = 'structured_cot'
    # tracking the accuracy of the model
    Correct_AI = 0
    Incorrect_AI = 0
    
    # Prepare files for the output 
    result_filename = f'Result/{CoT_style}_{model_name}.csv'
    if not data_bank.is_file_exits(result_filename):
        # Prepareing to save the results
        fields = ['text','ground_truth','sample_index','legal_principle','power_imbalance','consumer_harm','model_prediction','Human_AI_Alignment']
        data_bank.open_result_file(filename= result_filename, fields= fields)
    
    for i in cluases.itertuples(index=True):
       
        clause_text = i.text
        clause_answer = i.answer
        clause_index = i.index
        ith_result=[clause_text,clause_answer, clause_index] 
          
        prompt = prompt_bank.qurey_prompt('structured_cot_prompt',clause_text)
        print('prompt:\n', prompt, '\n-------------\n')
        
        model_output = model.qurey_LLM_model(user_prompt=prompt)
        model_output_processed = data_bank.josn_processing(model_output)

        ith_result.append(model_output_processed['legal_principle'])
        ith_result.append(model_output_processed['power_imbalance'])
        ith_result.append(model_output_processed['consumer_business_harm'])
        ith_result.append(model_output_processed['final_decision'])
        
        if clause_answer == model_output_processed['final_decision']:
            ith_result.append(1)
            Correct_AI = +1
        else:
            ith_result.append(0)
            Incorrect_AI = +1
       
        data_bank.save_result(result_filename,ith_result)
        
    return Correct_AI, Incorrect_AI

        
