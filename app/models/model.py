# to get the user results 
def carbon_footprint(transpo, rec, anim, en):
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
    if en == "okay":
        score = score + 30
    if en == "poor":
        score = score + 15
    
    if score >= 0 and score <= 21:
        return "low"
    elif score > 21 and score < 63:
        return "medium"
    elif score >= 63 and score <= 83:
        return "high"
        
def suggestion(transpo, rec, anim, en):
    sugg = {}
    if transpo == 'bus' or transpo == 'train' or transpo == 'boat' or transpo == 'plane' or transpo == 'car':
        sugg.update({"1" : "Based on your answers, why don't you try a different method of transportation like walking more often or using a bicycle."})
    if rec == "no":
        sugg.update({"2" : "Recycling is one small thing that makes a huge difference. When possible, try recycling more."})
    if anim != "never":
        sugg.update({"3" : "Farms easily use up a lot of resources and are working to become more efficient but a more conscious decision is to try eating less animal products."})
    if en != "efficient":
        sugg.update({"4" : "Your housing is not very efficient. If possible we suggest you try improving your household with more energy efficient methods."})
    if not sugg:
        sugg.update({"good" : "You are on the right path, keep on doing what you are doing."})
    return sugg

    
    