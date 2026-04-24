texcount $(
    find . -name "*.tex" ! \
    -name "*appendix1*" ! \
    -name "*abstract*" ! \
    -name "*abbreviations*"
) | grep "Words in text: "