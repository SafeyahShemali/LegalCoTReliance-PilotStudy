import model
import prompt_bank
import experiments as exp
import data_bank
import model as m


def main():      
    print('Structured_CoT Exp')
    #Data Processing
    dataset = data_bank.load_sample_data()

    #Set-Up the model
    model_name = "llama3.1:8b-instruct-q4_K_M" 
    model_key = "ollama"
    model_base_url = "http://localhost:11434/v1/"
    model = m.Model(model_name,model_key,model_base_url)
     
    # Experiment Part
    Correct_AI, Incorrect_AI = exp.task_with_structured_CoT(dataset, model, model_name)

    # Calculat the accuracy
    print('Correct_AI:\t', Correct_AI)
    print('Incorrect_AI:\t', Incorrect_AI)

if __name__=="__main__":
    main()
    