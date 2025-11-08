from utils import FrequencyNode, appendWithOrder
from collections import Counter as frequencies


def huffman(s: str):
    """
    Builds a Huffman coding tree from the input string.
    
    Args:
        s: Input string to analyze
        
    Returns:
        FrequencyNode representing the root of the Huffman tree
    """
    count = frequencies(s)
    count = sorted([FrequencyNode(key, count[key]) for key in count])
    head = FrequencyNode()
    
    # Handle edge case: single unique character
    if len(count) == 1:
        # Create a minimal tree with the single character on the right
        singleNode = count[0]
        head = FrequencyNode(val=singleNode.val, left=None, right=singleNode)
        return head
    
    while len(count) != 1:
        el1, el2 = count.pop(0), count.pop(0)
        newEl = el1 + el2
        head = newEl
        appendWithOrder(count, newEl)
    return head


def encode(s: str, tree: FrequencyNode = None):
    """
    Encodes a string using Huffman coding.
    
    Args:
        s: String to encode
        tree: Pre-built Huffman tree (if None, builds from s)
        
    Returns:
        Tuple of (encoded_string, huffman_tree)
        
    Raises:
        ValueError: If tree is provided but s contains characters not in the tree
    """
    if tree == None:
        tree = huffman(s)
    
    codes = tree.codes()
    print(codes)
    
    # Check if all characters in s are in the tree
    missingChars = set(c for c in s if c not in codes)
    if missingChars:
        raise ValueError(f"Characters not in tree: {missingChars}. "
                        f"Tree only contains: {set(codes.keys())}")
    
    return "".join(codes[c] for c in s), tree


def decode(code: str, tree: FrequencyNode):
    """
    Decodes a Huffman-encoded string.
    
    Args:
        code: Binary string to decode
        tree: Huffman tree used for encoding
        
    Returns:
        Decoded string
    """
    res = ""
    l, r = 0, len(code)
    codes = {
        value: key for key, value in tree.codes().items()
    }
    while l < r:
        if code[l: r] in codes:
            res += codes[code[l: r]]
            l = r
            r = len(code)
        else:
            r -= 1
    return res


if __name__ == "__main__":
    print("=" * 60)
    print("HUFFMAN ENCODING - Interactive Tool")
    print("=" * 60)
    
    s = input("\nEnter string to encode: ")
    
    try:
        code, tree = encode(s)
        
        print("\n" + "-" * 60)
        print("RESULTS:")
        print("-" * 60)
        print(f"Original string: {s}")
        print(f"Encoded binary:  {code}")
        print(f"Compression:     {len(s) * 8} bits → {len(code)} bits ({len(code) / (len(s) * 8) * 100:.1f}%)")
        
        print("\n" + "-" * 60)
        print("HUFFMAN TREE:")
        print("-" * 60)
        print(tree)
        
        print("\n" + "-" * 60)
        print("CHARACTER CODES:")
        print("-" * 60)
        codes = tree.codes()
        for char, codeStr in sorted(codes.items()):
            if char != '':
                print(f"  '{char}' → {codeStr}")
        
        print("\n" + "=" * 60)
        print("ENCODE MORE STRINGS (using same tree)")
        print("=" * 60)
        print("Type 'quit' or 'exit' to stop\n")
        
        while True:
            s = input("String to encode: ")
            
            if s.lower() in ['quit', 'exit', 'q']:
                print("\nGoodbye!")
                break
            
            if not s:
                continue
                
            try:
                code, _ = encode(s, tree)
                print(f"  → {code}")
            except ValueError as e:
                print(f"  ✗ Error: {e}")
                
    except ValueError as e:
        print(f"\n✗ Error: {e}")
    except KeyboardInterrupt:
        print("\n\nInterrupted. Goodbye!")