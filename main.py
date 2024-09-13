def prob_a_or_b(a,b,all_possible_outcomes):
    prob_a=len(a)/len(all_possible_outcomes)
    prob_b=len(b)/len(all_possible_outcomes)

    inter=a.intersection(b)
    prob_inter=len(inter)/len(all_possible_outcomes)
   
    return(prob_a + prob_b - prob_inter)

events={2,4,6}
greaterthan_two={3,4,5,6}
all_possible_rolls={1,2,3,4,5,6}

print("probablity of getting an even number or a number greater than 2")
print(prob_a_or_b(events,greaterthan_two,all_possible_rolls))