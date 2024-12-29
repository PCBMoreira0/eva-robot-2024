# # VM global variables
# root = {}
# script_node = {}
# links_node = {}
# fila_links =  [] # Link queue (commands)
# thread_pop_pause = False
import threading


play = False # Play status of the script. This variable has an influence on the function. link_process
# script_file = "" # Variable that stores the pointer to the xml script file on disk.
exec_comand_event = threading.Event()

# def update_root(newVal):
#     global root
#     root = newVal

# def update_script_node(newVal):
#     global script_node
#     script_node = newVal

# def update_links_node(newVal):
#     global links_node
#     links_node = newVal

# def update_fila_links(newVal):
#     global fila_links
#     fila_links = newVal

def get_play():
    return play

def update_play(newVal):
    global play
    play = newVal

def get_event():
    return exec_comand_event