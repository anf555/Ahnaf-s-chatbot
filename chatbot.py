# This code is made by Ahnaf
# DO NOT COPY/USE WITHOUT ANY PERMISSION FROM THE ORIGINAL OWNER (Ahnaf)

# Import Necessery Files / Library
from badword_filter import *
from wordvariable import *
import logging
import time

# Logging Function
logging.basicConfig(level=logging.INFO, filename="server.log", filemode="a", format="%(asctime)s - %(message)s")

def prompt(input, user):
    logging.info("Prompt Request : '" + str(input) + "' by : " + str(user))
    # Remove Any Excessive Space and Convert The Prompt to lowercase
    input2 = str(input)
    prompt_1 = input2.lower()
    prompt_2 = prompt_1.replace("  ", " ")
    prompt_3 = prompt_2.replace("   ", " ")
    prompt_4 = prompt_3.replace("    ", " ")
    prompt_5 = prompt_4.replace("     ", " ")
    prompt_6 = prompt_5.replace("      ", " ")
    # Badword Detection
    badword_stat = "no-badword"
    for word in badword:
        if prompt_6 == word:
            badword_stat = "badword-detected"
        elif prompt_6.__contains__(word):
            badword_stat = "badword-detected"
        else:
            pass
    if badword_stat == "badword-detected":
        logging.info("Badword Detected !")
        final_prompt = "badword-detected"
        with open('badword.txt', 'a') as f:
            f.write(time.asctime() + " : Badword Detection triggered by : " + user)
            f.writelines('\n')
            f.write("Prompt : " + prompt_6)
            f.writelines('\n')
            f.write("====================================================")
            f.close()
        return "badword-detected"
        final_prompt = "badword-detected"
    else:
        final_prompt = prompt_6

    # Analyzing for prompt responds
    for words in wordpack:
        try:
            words[final_prompt]
            check_trained ="yes"
        except:
            check_trained = ""
    if check_trained == "":
        if final_prompt == "badword-detected":
            responds_final = "badword-detected"
            return responds_final
        else:
            responds_final = default_responds["cannot_recognize"]
            logging.info("New unrecoqnized word : '" + str(prompt_6) + "' by : " + str(user))
            return responds_final
    else:
        responds_final = ""
        for words in wordpack:
            try:
                responds_final = responds_final + words[final_prompt]
            except:
                pass
        logging.info("Successfully responded to prompt | respond : " + responds_final)
        return responds_final