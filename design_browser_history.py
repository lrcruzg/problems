
# https://leetcode.com/problems/design-browser-history/

class BrowserHistory:
	def __init__(self, homepage: str):
		self.pages = [homepage]  # stack of visited pages
		self.i = 0  # index of the current page (in self.pages)
		self.len = 1  # length of the current stack of pages 
					  # (not every page in self.pages is reachable)

	def visit(self, url: str) -> None:
		if self.i == len(self.pages) - 1:
			self.pages.append(url)
			self.len += 1
		else:  # "unreachable" pages are not deleted immediately, 
			   # they're just ignored until its space is needed
			self.pages[self.i + 1] = url
			self.len = self.i + 2

		self.i += 1

	def back(self, steps: int) -> str:
		if self.i - steps >= 0:
			self.i -= steps
		else:
			self.i = 0

		return self.pages[self.i]

	def forward(self, steps: int) -> str:
		if self.i + steps < self.len:
			self.i += steps
		else:
			self.i = self.len - 1

		return self.pages[self.i]
