# get filder name from arguements
folder_name=$1

# slugify function
slugify () {
    echo "$folder_name" | iconv -t ascii//TRANSLIT | sed -r s/[~\^]+//g | sed -r s/[^a-zA-Z0-9]+/_/g | sed -r s/^-+\|-+$//g | tr A-Z a-z
}
file_name=`slugify`

# make new directory
mkdir "$folder_name"

# create files
touch "$folder_name/${file_name}.py" "$folder_name/${file_name}_test.py" "$folder_name/README.md"