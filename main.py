global remaining
global active_node
global active_edge
global active_length
global end
global suffix_link_lookup

class node:
    def __init__(self):
        # self.string = string # here just in case needed
        self.letters = dict()
        self.letter = None
        self.kids = dict()
        self.beg_index = 0
        self.terminal = -1
        self.suffix_link = None

remaining = 0
active_node = node()
active_edge = 0
active_length = 0
end = -1
suffix_link_lookup = dict()
        
def make_tree(word):
    global remaining
    global active_node
    global active_edge
    global active_length
    global end
    global suffix_link_lookup
    root = active_node
    i = 0
    new_phase = True
    # pointer = None
    while i < len(word):
        # everytime it's a new phase
        if new_phase:
            remaining += 1
            end += 1
            new_phase = False
        if active_length == 0:
            if word[i] not in active_node.letters:
                active_node.kids[i] = None
                active_node.letters[word[i]] = i
                remaining -= 1
            else:
                # active_edge = active_node.letters[word[i]]
                active_length += 1
                if active_edge != None:
                    if active_node.terminal < active_length:
                        edge = active_node.letters[word[i]]
                        active_node = active_node.kids[edge]
                        active_edge = edge
                        # or active_edge = active_node.beg_index
                i += 1
                end += 1
                remaining += 1
        else:
            if word[active_length] != word[i]:
                child = node()
                active_node.kids[active_edge] = child
                # child.string = word[active_edge, active_length - 1]
                child.letter = word[i]
                child.kids[active_length+1] = None
                child.letters[word[active_length+1]] = active_length+1
                child.kids[i] = None
                child.letters[word[i]] = i
                child.beg_index = active_edge
                child.terminal = active_length
                remaining -= 1
                if (child.beg_index, child.terminal) not in suffix_link_lookup:
                    child.suffix_link == root
                    suffix_link_lookup[child.beg_index, child.terminal] == child
                # elif i != len(word) - 1:
                else:
                    node = suffix_link_lookup.get(child.beg_index, child.terminal)
                    node.suffix_link = child
                    child.suffix_link = root
                    suffix_link_lookup[child.beg_index, child.terminal] == child
            if remaining != 0:
                if active_node != root:
                    active_node = active_node.suffix_link
                else: 
                    active_edge += 1
                    # or decrease by 1? @18:40
                    # said decrease by 1 @29.23
                    active_length -= 1
        if remaining == 0:
            i += 1
            new_phase = True

make_tree("xyzxaxyz$")