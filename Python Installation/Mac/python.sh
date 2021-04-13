if ! command -v brew &>/dev/null; then
  echo "Installing Homebrew, an OSX package manager, follow the instructions..." 
  ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

else
  echo "You already have Homebrew installed...good job!"; fi

echo "Installing Python"
brew install python3