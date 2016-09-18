# basic answer, only one synonym for each word and synonyms are only one word long
def make_synDict(syns):
    ans = {}
    for w1, w2 in syns:
        ans.setdefault(w1, w2)
        ans.setdefault(w2, w1)
    return ans

def check_equal(cmds, syns):
    ans = []
    synDict = make_synDict(syns)
    for c1, c2 in cmds:
        eq = True
        if c1 == c2:
            ans.append(True)
            continue
        cL1 = c1.split(' ')
        cL2 = c2.split(' ')
        if len(cL1) != len(cL2):
            ans.append(False)
            continue
        for w1, w2 in zip(cL1, cL2):
            if w1 != w2:
                if w1 in synDict:
                    if synDict[w1] == w2:
                        continue
                    eq = False
                    break
        ans.append(eq)
    return ans

# more advanced answer -- thanks to Erich Wellinger
from collections import defaultdict
def make_trans_syn_dict(syn_list):
    def _make_syn_dict(syn_list):
        d = defaultdict(set)
        for w1, w2 in syn_list:
            d[w1].add(w2)
            d[w2].add(w1)
        return d

    def _get_connected_component(graph, starting_node):
        visited, seen = set(), {starting_node}
        queue = [starting_node]
        while queue:
            node = queue.pop()
            if node not in visited:
                visited.add(node)
                neighbors_to_add = graph[node].difference(seen)
                queue.extend(neighbors_to_add)
                seen.update(neighbors_to_add)
        return visited

    d = _make_syn_dict(syn_list)
    nodes = set(d.keys())
    trans_dict = {}

    while nodes:
        node = nodes.pop()
        component = _get_connected_component(d, node)
        for node in component:
            trans_dict[node] = component.difference(node)
        nodes = nodes.difference(component)
    return trans_dict

def check_equal_adv(cmds, syns):
    ans = []
    synDict = make_trans_syn_dict(syns)
    for c1, c2 in cmds:
        eq = True
        if c1 == c2:
            ans.append(True)
            continue
        cL1 = c1.split(' ')
        cL2 = c2.split(' ')
        if len(cL1) != len(cL2):
            ans.append(False)
            continue
        for w1, w2 in zip(cL1, cL2):
            if w1 != w2:
                if w1 in synDict:
                    if w2 in synDict[w1]:
                        continue
                    eq = False
                    break
        ans.append(eq)
    return ans

if __name__ == "__main__":
    testCmds = [('eat some apples', 'consume some apples'), ('eat many apples', 'destroy some apples')]
    testSyns = [('eat', 'consume'), ('many', 'lots')]
    print check_equal(testCmds, testSyns)
    # run time is O(NML) where N is length of the commands list,
    # M is the length of the synonyms list, and L is the
    # average length of a command
    # space complexity is O(NM) because we build a dict of synonyms and a list
    # for our answer

    # now with multiple synonyms for words
    testCmds = [('eat some apples', 'ingest some apples'), ('eat many apples', 'destroy some apples')]
    testSyns = [('eat', 'consume'), ('many', 'lots'), ('consume', 'ingest')]
    print check_equal_adv(testCmds, testSyns)

    # big O time complexity is still O(NML) since we go through the synonyms and
    # commands once and may have to go through each word of each command sometimes
    # I'm not sure if using symmetric difference on the commands would be of use here,
    # since we could have repeat words http://stackoverflow.com/questions/15455737/python-use-set-to-find-the-different-items-in-list
    # and we would have to go through each element of the list of words in the command
    # to build the set anyway
    # big O space complexity is still O(NM) as well
