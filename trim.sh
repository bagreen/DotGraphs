mkdir trimmed
for f in *.txt
do
	awk '{$1=""; sub(" ", " "); print}' $f > newFile.txt
	touch newerFile.txt
	python pyTrim.py
	mv newerFile.txt trimmed/newerFile.txt
	mv trimmed/newerFile.txt trimmed/$f
done
rm trimmed/newFile.txt
