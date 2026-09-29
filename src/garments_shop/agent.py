from ollama import chat

from garments_shop.tool_registry import ToolRegistry

from garments_shop.extract_memory import extract_memory

from garments_shop.memory import (load_memory, save_memory, get_memory, remember, forget)

from garments_shop.tools import (
    check,
    calculate_profit,
    calculate_loss,
    calculate_profit_per_unit,
    calculate_loss_per_unit)



def run_agent(user_message, messages, memory):
    new_memory = extract_memory(user_message)

    if memory:

        memory_text = str(memory)

    else:

        memory_text = "No saved memory."

    messages.append(
        {
            "role": "system",
            "content": f"""
You are a helpful personal assistant.

Here is the user's long-term memory:

{memory_text}

Use this information when it is relevant to the user's question.
Do not invent information that is not present in the memory.
"""
        }
    )

    # Add user message to conversation
    messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    tools = [ load_memory, save_memory, get_memory, remember, forget,check,
        calculate_profit,
        calculate_loss,
        calculate_profit_per_unit,
        calculate_loss_per_unit

    ]

    registry = ToolRegistry(tools)

    max_iteration = 10
    for iteration in range (max_iteration):

         response = chat(

        model = "qwen3:8b",
        messages = messages,
        tools = tools
    )
         messages.append(response.message)

         if not response.message.tool_calls:
           print ("Final Answer: ")
           return response.message.content

         for tool_call in response.message.tool_calls or []:

             function_name = tool_call.function.name    
             arguments = tool_call.function.arguments

             result = registry.execute(function_name, arguments)

             messages.append(
{
"role": "tool",
"tool_name": function_name,
"content": str(result)
})
    return "Agent stopped: maximum iterations reached."
