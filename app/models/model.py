# to get the user results 
def carbon_footprint(transpo, rec, anim):
    score = 0
    if transpo == 'bus' or transpo == 'train':
        # print(" you use a " +transpo+ " so the score increased by 8")
        score = score + 8
    if transpo == 'boat' or transpo == 'plane' or transpo == 'car':
        # print(" you use a " +transpo+ " so the score increased by 20")
        score = score + 20
    if anim == "occasionally":
        # print(" they eat animals occasionally so score increased by 10")
        score = score + 10
    if anim == "always":
        # print(" you eat animals always so score increased by 20")
        score = score + 20
    if rec == "no":
        # print(" you dont recycle so score increased by 13")
        score = score + 13 
    
    if score >= 0 and score <= 14:
        return "low"
    elif score >= 15 and score <= 39:
        return "medium"
    elif score >= 40 and score <= 53:
        return "high"