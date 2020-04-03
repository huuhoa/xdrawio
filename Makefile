render:
	./generate.py "CorePayment.xlsx" | pbcopy

pdf:
	rm -f cp.pdf
	./generate.py "CorePayment.xlsx" -po landscape > cp.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o cp.pdf cp.drawio
	open cp.pdf

ppr:
	rm -f ppr.pdf
	./generate.py "ppr.xlsx" > ppr.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o ppr.pdf ppr.drawio
	open ppr.pdf

bb:
	rm -f bank_binding.pdf
	./generate.py "/Users/huuhoa/Documents/CorePayment/orgchart/BankBinding.xlsx" > bank_binding.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o bank_binding.pdf bank_binding.drawio
	open bank_binding.pdf

status:
	rm -f bank_status.pdf
	./generate.py -t bank_status -ps A5 "/Users/huuhoa/Documents/CorePayment/orgchart/BankBinding.xlsx" > bank_status.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o bank_status.pdf bank_status.drawio
	open bank_status.pdf
