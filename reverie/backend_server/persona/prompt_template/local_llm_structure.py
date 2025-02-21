'''
Author: Wenchang Gao

File: local_llm_structure.py
Description: 
  Wrapper functions to interact with local LLM servers. Most communications 
  are done via socket. 
'''
import json 
import subprocess # TODO: Switch to socket and remove subprocess calling
import socket 


