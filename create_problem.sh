function leetpy() {
    inp="$@"
    # echo "input: $inp"
    problem=$(echo "$inp" | tr '[A-Z]' '[a-z]' | tr ' ' '-')
    # echo "problem: $problem"
    problem+=".py"
    cp /home/zpunix/prog_sym_link/leetcode_pset/py_template.py $problem
    echo "python $problem" | clip
    vim $problem
}
