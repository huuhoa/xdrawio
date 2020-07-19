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
	rm -f cp_bank_status.pdf
	./generate.py -t status -ps A5 CorePayment.xlsx > cp_bank_status.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o cp_bank_status.pdf cp_bank_status.drawio
	open cp_bank_status.pdf

status-svg:
	rm -f bank_status.svg
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f svg -o bank_status.svg bank_status.drawio

.PHONY: roadmap
roadmap:
	rm -f cp_roadmap.pdf
	./generate.py -t roadmap -ps A5 CorePayment.xlsx > cp_roadmap.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o cp_roadmap.pdf cp_roadmap.drawio
	open cp_roadmap.pdf

cp:
	./generate.py CorePayment.xlsx -po landscape > cp_features.drawio
	./generate.py -t status -ps A5 CorePayment.xlsx > cp_bank_status.drawio
	./generate.py -t roadmap -ps A5 CorePayment.xlsx > cp_roadmap.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o cp_roadmap.pdf cp_roadmap.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o cp_bank_status.pdf cp_bank_status.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o cp_features.pdf cp_features.drawio

arch:
	rm -f cp.pdf
	./generate.py -t arch "CorePayment.xlsx" -po landscape > cp.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o cp.pdf cp.drawio
	open cp.pdf

arch-test:
	@./generate.py -t arch "CorePayment.xlsx" -d True -po landscape

arch-test-1:
	@./generate.py -t arch layout.xlsx -d True -po landscape | ./layout.py -o layout.drawio
	@/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o layout.pdf layout.drawio
	@open layout.pdf

arch-test-2:
	@./generate.py -t arch CorePayment.xlsx -d True -po landscape | ./layout.py -o layout.drawio
	@/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o layout.pdf layout.drawio
	@open layout.pdf

arch-test-3:
	@./generate.py -e True -o layout1.drawio -t arch CorePayment.xlsx
	@/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o layout1.pdf layout1.drawio
	@open layout1.pdf

arch-test-4:
	@./generate.py -e True -lt layout1.json --write_layout_tree True -o layout1.drawio -t arch CorePayment.xlsx
	@/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o layout-level2.pdf layout1.drawio
	@open layout-level2.pdf

arch-test-5:
	@./generate.py -ps A3 -e True -lt layout1.json --write_layout_tree True -l 1 -o layout1.drawio -t arch CorePayment.xlsx
	@/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o layout-level1.pdf layout1.drawio
	@open layout-level1.pdf

arch-test-6:
	@./generate.py -ps A4 -po landscape -e True -lt layout1.json --write_layout_tree True -l 0 -o layout1.drawio -t arch CorePayment.xlsx
	@/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o layout-level0.pdf layout1.drawio
	@open layout-level0.pdf

test:
	python3 tests.py
