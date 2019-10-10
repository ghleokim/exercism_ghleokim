#!/usr/bin/env bash

main() {
  X="$1"
  if [ "$X" ]; then
    echo "One for $X, one for me."
  else
    echo "One for you, one for me."
  fi
}

main "$@"

# #!/usr/bin/env bash

# main() {
#   X="$1"
#   if [ "$X" == "" ]; then
#     echo "One for you, one for me."
#   else
#     echo "One for $X, one for me."
#   fi
# }

# main "$@"