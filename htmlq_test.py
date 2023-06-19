from htmlq import Htmlq

pyhtmlq = Htmlq()

file = "C:/Users/maxde/code/interpreting/aguila/billing/upcoming/pinga.html"

results = pyhtmlq.css(f"'span[id*=\"Birth\"]' -f {file}")

print('type:', type(results))
print('length:', len(results))
