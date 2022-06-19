def one_D_neighbors(num , bits):
    ans = []
    for i in range(bits):
        temp = ""
        for k in range(bits):
            if k == i:
                if num[i] == "0":
                    temp += "1"
                else:
                    temp += "0"
                temp+= num[i+1:bits]
                break
            else:
                temp += num[k]
        ans.append(temp)
    return ans

def neighbors(num , bits):
    ans = set(one_D_neighbors(num , bits))
    holder = ans.copy()
    for x in holder:
        ans = ans.union(one_D_neighbors(x , bits))
    ans.remove(num)
    return ans


def cluster(verticies , bits):
    clusters = []
    for element in verticies:
        clusters.append({element})
    for vertex in verticies:
        Neighbors = neighbors(vertex , bits)
        for neighbor in Neighbors:
            if neighbor in verticies:
                first_flag = False
                second_flag = False
                for i in range(len(clusters)):
                    if vertex in clusters[i]:
                        first_index = i
                        first_flag = True
                    if neighbor in clusters[i]:
                        second_index = i
                        second_flag = True
                    if first_flag and second_flag:
                        try:
                            if first_index != second_index:
                                if first_index < second_index:
                                    clusters.append(clusters.pop(first_index).union(clusters.pop(second_index-1)))
                                else:
                                    clusters.append(clusters.pop(first_index).union(clusters.pop(second_index)))
                        except UnboundLocalError:
                            continue
                        break

    return len(clusters)





verticies = set()
with open('clustering_big.txt') as f:
    first_line = f.readline()
    num , bits =  list(map(int,first_line[:-1].split()))
    data = f.readlines()
    for line in data:
        vertex = line[:-1]
        vertex = vertex.replace(" " ,"")
        verticies.add(vertex)
f.close()


print(cluster(verticies,bits))