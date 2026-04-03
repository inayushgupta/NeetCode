func groupAnagrams(strs []string) [][]string {
    groups := make(map[string][]string)

    for _, str := range strs {
        sortedString := SortString(str)
        if _, found := groups[sortedString]; found {
            groups[sortedString] = append(groups[sortedString], str)
        } else {
            groups[sortedString] = []string{str}
        }
    }

    var result  = [][]string{}

    for _, group := range groups {
        result = append(result, group)
    }

    return result

}


func SortString(s string) string {
	w := strings.Split(s, "")
	sort.Strings(w)
	return strings.Join(w, "")
}

