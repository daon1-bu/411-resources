BASE_URL="http://localhost:5000/api"

ECHO_JSON=false

while [ "$#" -gt 0 ]; do
  case $1 in
    --echo-json) ECHO_JSON=true ;;
    *) echo "Unknown parameter passed: $1"; exit 1 ;;
  esac
  shift
done

###############################################
#
# Health checks
#
###############################################

# Function to check the health of the service
check_health() {
  echo "Checking health status..."
  curl -s -X GET "$BASE_URL/health" | grep -q '"status": "success"'
  if [ $? -eq 0 ]; then
    echo "Service is healthy."
  else
    echo "Health check failed."
    exit 1
  fi
}

####################################################
#
# Basis functionality and error tests
#
####################################################

add_boxer() {
    name=$1
    weight=$2
    height=$3
    reach=$4
    age=$5

    echo "Adding boxer: $name , $weight , $height, $reach, $age"
    response=$(curl -s -X POST "$BASE_URL/add-boxer" \
        -H "Content-Type: application/json" \
        -d "{\"name\":\"$name\", \"weight\":\"$weight\", \"height\":$height, \"reach\":$reach, \"age\":$age}")

    if echo "$response" | grep -q '"status": "success"'; then
        echo "Boxer added succesfully."
        if [ "$ECHO_JSON" = true ]; then
        echo "boxer JSON:"
        echo "$response" | jq .
        fi
    else
        echo "Failed to add boxer."
        exit 1
    fi
}

fight() {
    echo "Initiating a fight"
    response=$(curl -s -X POST "$BASE_URL/fight")

    if echo "$response" | grep -q '"status": "success"'; then
        echo "Succesfully started a fight"
    else
        echo "Failed to start a fight"
        exit 1
    fi
}

add_third_boxer(){
    
}

