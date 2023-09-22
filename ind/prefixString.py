class Node(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.children = {}
		self.is_end = False


class Trie:
	def __init__(self, words):
		self.root = Node()
		self.words = words
		# initialise trie
		for word in words:
			self.insert(word)

	def insert(self, word):

		def _dfs(node, tmp):
			if len(tmp) == 0:
				node.is_end = True
				return

			if tmp[0] not in node.children:
				node_nxt = Node()
				node.children[tmp[0]] = node_nxt
				_dfs(node_nxt, tmp[1:])
			else:
				_dfs(node.children[tmp[0]], tmp[1:])
		_dfs(self.root, word)

	def find_prefix(self, prefix):
		ans = []

		def _dfs(node, prefix):
			if len(prefix) == 1 and prefix in node.children:
				return node
			_dfs(node.children[prefix[0]], prefix[1:])

		node = _dfs(self.root, prefix)
		q = [(node, prefix)]
		while len(q) > 0:
			node, prefix = q.pop(0)
			if node.is_end:
				ans.append(prefix)
			for char, child_node in node.children.items():
				q.append((child_node, prefix+char))
		return ans

if __name__ == "__main__":
	def test():
		outer = 1
		def _inner():
			print("outer is: ", outer)
		_inner()

	test()







		