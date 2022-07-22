import re
import random

class SupportBot:
  negative_responses = ("nothing", "don't", "stop", "sorry")

  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

  def __init__(self):
    self.matching_phrases = {'how_to_pay_bill': [r'.*how.*pay bills.*', r'.*how.*pay my bill.*'], r'pay_bill': [r'.*want.*pay.*my.*bill.*account.*number.*is (\d+)', r'.*need.*pay.*my.*bill.*account.*number.*is (\d+)']}

  def welcome(self):
    self.name = input("Welcome, I'm a Cardiopulmonary Resuscitation virtual assistant. Before I can help you, I need some information from you. What is your name? ")
    
    will_help = input(f"Ok {self.name}, what can I help you with? ")
    
    if will_help in self.negative_responses:
      print("Ok, have a great day and stay safe during the COVID-19 pandemic")
      return
    
    self.handle_conversation(will_help)
  
  def handle_conversation(self, reply):
    while not self.make_exit(reply):
      #reply = input("How can I help you?") ### Linha de teste
      reply = input(self.match_reply(reply))
      
  def make_exit(self, reply):
    for exit_command in self.exit_commands:
      if exit_command in reply:
        print("Ok, have a great day!")
        return True
      
    return False
  
  def match_reply(self, reply):
    for key, values in self.matching_phrases.items():
      for regex_pattern in values:
        found_match = re.match(regex_pattern, reply.lower())
        if found_match and key == 'how_to_reanimate':
          return self.check_first_signs()
        elif found_match and key == 'pay_bill':
          return self.pay_bill_intent(found_match.groups()[0])
        
    return input("I did not understand you. Can you please ask your question again?")
  
  def check_first_signs(self):
    response =  input(f"Please verify the following signs of the person: \n 1) Cold skin and yellow; \n 2) Dilated pupils; \n 3) Unconsciousness; \n 4) Absence of heartbeat; \n 5) Absence of breathing. Did you check all the signs above and confirm them, {self.name}? ")
    return self.perform_cpr_procedure()
  
  def perform_cpr_procedure(self):
    response = input("Let's perform a CPR while waiting and ask a family member to call the paramedic. Okay ?")
    return self.procedure()

  def procedure(self):
    return "Procedure: \n 1. Lay the person who is face up on a rigid and firm surface; \n 2. Kneel beside the victim and locate the center of the chest, more specifically on the line between the nipples; \n 3. extend your arms, overlap your hands and intertwine the fingers of the upper hand, involving the lower hand; \n 4. Start the compressions by pressing down on the victim's chest; \n 5. Always keep your arms straight and constantly compress the victim's chest, paying attention to the correct rhythm and depth."
  
# Create a SupportBot instance
SupportConversation = SupportBot()
# Call the .welcome() method
SupportConversation.welcome()


