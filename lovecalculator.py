def love():
    singleness = 0
    maturity = 0
    intelligence = 0
    trust = 0
    love_score = 0

    # Get singleness score
    while singleness != 1:
        singleness = input("Enter your singleness score (must be 1): ")
        try:
            singleness = int(singleness)
            if singleness != 1:
                print("Kindly input the number 1 here")
        except:
            print("Kindly input a number between 1 and 10")
            singleness = 0

    # Get maturity, intelligence, trust, and love scores
    while True:
        maturity = input("Enter your maturity score (between 1 and 10): ")
        intelligence = input("Enter your intelligence score (between 1 and 10): ")
        trust = input("Enter your trust score (between 1 and 10): ")
        love_score = input("Enter your love score (between 1 and 10): ")

        try:
            maturity = int(maturity)
            intelligence = int(intelligence)
            trust = int(trust)
            love_score = int(love_score)
            if 1 <= maturity <= 10 and 1 <= intelligence <= 10 and 1 <= trust <= 10 and 1 <= love_score <= 10:
                break
            else:
                print("Kindly input a number between 1 and 10")
        except:
            print("Kindly input a number between 1 and 10")

    total_score = singleness + maturity + intelligence + trust + love_score

    if total_score >= 21:
        print("Congrats! You are closer to your desired romantic relationship")
    else:
        print("You need to work on your scores. Total score must be at least 21")
love()
