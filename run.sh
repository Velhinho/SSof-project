if [ $# == 0 ]; then
    echo "Usage: $0 param1"
    echo "* param1: ex. 3a, 4b"
    exit 1
fi

slice_file=`find slices_ast/ -name "*$1*"`
pattern_file=`find patterns/ -name "*$1*"`
python3 main.py $slice_file $pattern_file