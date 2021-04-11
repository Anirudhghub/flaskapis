
# Ask for initial State from User
initial_state=int(input("Enter the initial Value of whole transaction"))
print("There will be two process p1 and p2 you have entered value ",initial_state," as initial State of whole transaction")
# Asking for process P1 state 
p1_initial_value=int(input("Enter initial value  less than "+str(initial_state)+" :  "))
p2_initial_value=initial_state-p1_initial_value
print("P1 initial value :  "+str(p1_initial_value)+"\nP2 initial value :  "+str(p2_initial_value))
timestamp_input=int(input("Enter the number of time instances :  "))
# Asking for Time stamp
timestamps=[i+1 for i in range(0,timestamp_input)]
for i in timestamps:
    print("t"+str(i))

# Asking for number of messages  during transactions
message_count_user=int(input("Enter the number of message you want to involve in the Algorithm"))
transactions=[]
# Asking for info While sending message from P1 to P2 or vice versa
for i in range(0,message_count_user):
    user_process_choice=int(input("Press 1 if messgae will be sent by process P1\nPress 2 if messgae will be sent by process P2 :  "))
    transaction_instance={}
    if(user_process_choice==1):
        transaction_instance["process"]=1
        transaction_instance["start"]=int(input("enter the time stamp after which the message will be sent from process P1 :  "))
        transaction_instance["end"]=int(input("enter the time stamp after which the message will be received on process P2 :  "))
        transaction_instance["message"]=int(input("Enter number between 1 and "+str(p1_initial_value)+" :  "))
        p1_initial_value=p1_initial_value-transaction_instance["message"]
        transaction_instance["process_values"]=p1_initial_value
        
    if(user_process_choice==2):
        transaction_instance["process"]=2
        transaction_instance["start"]=int(input("enter the time stamp after which the message will be sent from process P2 :  "))
        transaction_instance["end"]=int(input("enter the time stamp after which the message will be received on process P1 : "))  
        transaction_instance["message"]=int(input("Enter number between 1 and "+str(p2_initial_value)+" :  "))
        p2_initial_value=p2_initial_value-transaction_instance["message"]
        transaction_instance["process_values"]=p2_initial_value
    transactions.append(transaction_instance)

# Sort of asking for initialization of marker message
time_instance=int(input("Enter time instance between 1 to "+str(timestamp_input)+" at which you want to start recording"))

resultant=0
info_string=""
temp=0
# Getting resultatnt on the basis of Algorithim
for i in range(0,len(transactions)):
    if(time_instance==transactions[i]['start']):
        print()
        info_string+="Time Stamp while starting = t"+str(transactions[i]["start"])+"\n"
        resultant+=transactions[i]['process_values']
        info_string+="Local state of Process p"+str(transactions[i]["process"])+"="+str(transactions[i]['process_values'])+"\n"
        resultant+=transactions[i]['message']
        info_string+="Value Channel from p"+str(transactions[i]["process"])+" is "+str(transactions[i]['message'])+"\n"
        temp=transactions[i]['end']
    if(temp==transactions[i]['start']):
        info_string+="Time Stamp  ending at = t"+str(transactions[i]["end"])+"\n"
        info_string+="Local state of Process p"+str(transactions[i]["process"])+"="+str(transactions[i]['process_values'])+"\n"
        resultant+=transactions[i]['process_values']
        info_string+="Value Channel from p"+str(transactions[i]["process"])+" is "+str(transactions[i]['message'])+"\n"
        resultant+=transactions[i]['message']
        break

print("Initial Value"+str(initial_state))
print("Value after getting snapshot"+str(resultant))
print(info_string)
