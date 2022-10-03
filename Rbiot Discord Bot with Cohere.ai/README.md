Pipeline
=============================
1. Gather previous messages from raphraphraph, luckyjalien, and nil
2. Clean messages and put them into a dataframe
3. Process messages into embeddings
    * Send messages (before embeddings) to cohere.ai to finetune already made models
    * Test Results
4. Use finetuned moddel to run with a discord bot command.
    * Input: A message
    * Output: The person most likely to type that message between raphraphraph, luckyjalien, and nil
