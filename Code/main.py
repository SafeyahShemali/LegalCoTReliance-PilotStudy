import model
import prompt_bank
import experiments as exp
import data_bank
import model as m
import time


def main():  
    
    #Data Processing
    dataset = data_bank.load_data()

    for i in ["llama3.1:8b-instruct-q4_K_M"]: #llama3.2:3b-instruct-q4_K_M
        #Set-Up the model
        model_name =  i
        model_key = "ollama"
        model_base_url = "http://localhost:11434/v1/"
        model = m.Model(model_name,model_key,model_base_url)
        
        #do the exp 
        CoT_style = 'concise_cot'
        start_time = time.time()
        exp.task_with_concise_CoT(dataset, model, model_name)
        print('---------------------')
        print('task_with_concise_CoT: ',time.time() - start_time)
        
        # start_time = time.time()
        # exp.task_with_structured_CoT(dataset, model, model_name)
        # print('task_with_structured_CoT: ',time.time() - start_time)

        # calculat the accuracy
        legalBench_accuracy = 0.8224
        result_file_path = f'../Result/{CoT_style}_{model_name}.csv'
        result = data_bank.load_result_data(result_file_path)
        AI_correct_count= result['Human_AI_Alignment'].sum()
        N = len(result)
        test_accuracy = AI_correct_count/N
        print(AI_correct_count,N,test_accuracy)
        if abs(legalBench_accuracy-test_accuracy) <= 0.3:
            print('Good model')


if __name__=="__main__":
    main()
    