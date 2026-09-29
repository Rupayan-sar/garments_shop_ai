class ToolRegistry:

   def __init__(self, tools):
       
       self.tools = {
       tool.__name__: tool
       for tool in tools
}
   def get(self, name):
       
       return self.tools.get(name)
   
   def execute(self, name, arguments):

       function = self.get(name)

       if function is None:
            return f"Unknown tool: {name}"
       
       else:
            try:
       
                return function(**arguments)
       
            except Exception as e:
               return f"Tool failed: {e}"