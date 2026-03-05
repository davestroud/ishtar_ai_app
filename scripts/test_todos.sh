#!/bin/bash

# Test script for Todo feature integration
# This script verifies that the todo interface can connect to the backend API

echo "========================================"
echo "Todo Feature Integration Test"
echo "========================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

API_URL="http://localhost:8000"
FRONTEND_URL="http://localhost:8080"

# Function to check if a service is running
check_service() {
    local url=$1
    local name=$2

    if curl -s --head --request GET "$url" | grep "200 OK\|404 Not Found" > /dev/null; then
        echo -e "${GREEN}✓${NC} $name is running at $url"
        return 0
    else
        echo -e "${RED}✗${NC} $name is NOT running at $url"
        return 1
    fi
}

# Function to test API endpoint
test_endpoint() {
    local method=$1
    local endpoint=$2
    local name=$3

    response=$(curl -s -o /dev/null -w "%{http_code}" -X "$method" "$API_URL$endpoint")

    if [ "$response" = "200" ] || [ "$response" = "404" ]; then
        echo -e "${GREEN}✓${NC} $name: $method $endpoint (Status: $response)"
        return 0
    else
        echo -e "${RED}✗${NC} $name: $method $endpoint (Status: $response)"
        return 1
    fi
}

# Check backend API
echo "1. Checking Backend API (ishtar_ai)..."
echo "----------------------------------------"
if check_service "$API_URL" "Backend API"; then
    echo ""
    echo "   Testing API endpoints..."
    test_endpoint "GET" "/todos" "List todos"
    test_endpoint "GET" "/docs" "API documentation"
else
    echo -e "${YELLOW}   To start the backend:${NC}"
    echo "   cd /Users/davidstroud/ishtar_ai"
    echo "   source .venv/bin/activate"
    echo "   uvicorn app.main:app --reload --port 8000"
fi

echo ""
echo "2. Checking Frontend App (ishtar_ai_app)..."
echo "----------------------------------------"
if check_service "$FRONTEND_URL" "Frontend App"; then
    echo ""
    echo "   Testing frontend routes..."
    response=$(curl -s -o /dev/null -w "%{http_code}" "$FRONTEND_URL/todos")
    if [ "$response" = "200" ]; then
        echo -e "${GREEN}✓${NC} Todo page accessible: /todos (Status: $response)"
    else
        echo -e "${RED}✗${NC} Todo page NOT accessible: /todos (Status: $response)"
    fi
else
    echo -e "${YELLOW}   To start the frontend:${NC}"
    echo "   cd /Users/davidstroud/ishtar_ai_app"
    echo "   source .venv/bin/activate"
    echo "   uvicorn app.main:app --reload --port 8080"
fi

echo ""
echo "3. File Structure Check..."
echo "----------------------------------------"
files=(
    "/Users/davidstroud/ishtar_ai_app/app/templates/todos.html"
    "/Users/davidstroud/ishtar_ai_app/app/static/js/todos.js"
    "/Users/davidstroud/ishtar_ai_app/TODO_FEATURE.md"
)

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓${NC} $(basename "$file") exists"
    else
        echo -e "${RED}✗${NC} $(basename "$file") NOT found"
    fi
done

echo ""
echo "========================================"
echo "Test Complete"
echo "========================================"
echo ""
echo "Next Steps:"
echo "1. Ensure both services are running"
echo "2. Visit: $FRONTEND_URL/todos"
echo "3. Test creating, updating, and deleting tasks"
echo ""
