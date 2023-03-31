if [[ $RESPONSE == *"HTTP/1.1 200 OK"*  ]]; then
    echo "Successful response from docker"
else
    echo "Test failed"
fi