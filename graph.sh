awk '{$1=""; sub(" ", " "); print}' ben/.bash_history > ben/3.dot
dot -Tpdf ben/3.dot > ben/3.pdf