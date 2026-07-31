environments = ["dev", "prod", "dev", "staging", "prod", "dev"]

count = []

for env in environments:
    if env not in count:
        count.append(env)
        count.append(1)
    else:
        pos = count.index(env)
        count[pos+1] += 1

print(count)
