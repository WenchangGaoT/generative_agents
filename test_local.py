'''
Test LLMs running locally
'''

from transformers import AutoTokenizer, AutoModelForCausalLM


if __name__ == '__main__':
    messages = [] 
    model_path = '/root/.cache/huggingface/hub/models--deepseek-ai--DeepSeek-R1-Distill-Llama-8B'
    model_path = 'deepseek-ai/DeepSeek-R1-Distill-Llama-8B'
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)
    while True: 
        msg = input('You: ')
        if msg.lower() == 'exit': 
            break 
        messages.append(
            {'role': 'user', 'content': msg}
        )
        msg_emb = tokenizer(msg, return_tensors='pt')
        print('embeddings: ', msg_emb)
        response_ids = model.generate(msg_emb.input_ids)
        print('Generate ids: ', response_ids)
        response = tokenizer.batch_decode(response_ids)
        print('Response: ', response)
