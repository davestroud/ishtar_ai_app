// Todo Manager JavaScript
// API Base URL - configure based on environment
const API_BASE_URL = 'http://localhost:8000';

// State
let todos = [];
let currentFilter = 'all';

// DOM Elements
const todosGrid = document.getElementById('todos-grid');
const emptyState = document.getElementById('empty-state');
const loadingState = document.getElementById('loading-state');
const addTodoForm = document.getElementById('add-todo-form');
const filterTabs = document.querySelectorAll('.filter-tab');
const toast = document.getElementById('toast');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    setupEventListeners();
    fetchTodos();
});

// Setup Event Listeners
function setupEventListeners() {
    // Form submission
    addTodoForm.addEventListener('submit', handleAddTodo);

    // Filter tabs
    filterTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const filter = tab.dataset.filter;
            setActiveFilter(filter);
        });
    });

    // Keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        // Escape to clear form
        if (e.key === 'Escape') {
            addTodoForm.reset();
            document.getElementById('todo-title').blur();
        }
    });
}

// API Functions
async function fetchTodos() {
    try {
        showLoading();
        const response = await fetch(`${API_BASE_URL}/todos`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        todos = data.todos || [];
        renderTodos();
        updateCounts();
        hideLoading();
    } catch (error) {
        console.error('Error fetching todos:', error);
        showToast(`Failed to load tasks: ${error.message}`, 'error');
        hideLoading();
        showEmptyState();
    }
}

async function createTodo(title, description, status) {
    try {
        const response = await fetch(`${API_BASE_URL}/todos`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title: title,
                description: description || '',
                status: status,
            }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        todos.unshift(data);
        renderTodos();
        updateCounts();
        showToast('Task created successfully', 'success');
        return data;
    } catch (error) {
        console.error('Error creating todo:', error);
        showToast(`Failed to create task: ${error.message}`, 'error');
        throw error;
    }
}

async function updateTodo(id, updates) {
    try {
        const response = await fetch(`${API_BASE_URL}/todos/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updates),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        const index = todos.findIndex(t => t.id === id);
        if (index !== -1) {
            todos[index] = data;
        }
        renderTodos();
        updateCounts();
        showToast('Task updated successfully', 'success');
        return data;
    } catch (error) {
        console.error('Error updating todo:', error);
        showToast(`Failed to update task: ${error.message}`, 'error');
        throw error;
    }
}

async function deleteTodo(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/todos/${id}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        todos = todos.filter(t => t.id !== id);
        renderTodos();
        updateCounts();
        showToast('Task deleted successfully', 'success');
    } catch (error) {
        console.error('Error deleting todo:', error);
        showToast(`Failed to delete task: ${error.message}`, 'error');
        throw error;
    }
}

// Event Handlers
async function handleAddTodo(e) {
    e.preventDefault();

    const title = document.getElementById('todo-title').value.trim();
    const description = document.getElementById('todo-description').value.trim();
    const status = document.getElementById('todo-status').value;

    if (!title) {
        showToast('Please enter a task title', 'error');
        return;
    }

    try {
        await createTodo(title, description, status);
        addTodoForm.reset();
        document.getElementById('todo-title').focus();
    } catch (error) {
        // Error already handled in createTodo
    }
}

async function handleStatusChange(id, newStatus) {
    try {
        await updateTodo(id, { status: newStatus });
    } catch (error) {
        // Error already handled in updateTodo
    }
}

async function handleDelete(id) {
    if (confirm('Are you sure you want to delete this task?')) {
        try {
            await deleteTodo(id);
        } catch (error) {
            // Error already handled in deleteTodo
        }
    }
}

// Render Functions
function renderTodos() {
    const filteredTodos = getFilteredTodos();

    if (filteredTodos.length === 0) {
        showEmptyState();
        return;
    }

    hideEmptyState();
    todosGrid.innerHTML = filteredTodos.map(todo => createTodoCard(todo)).join('');

    // Attach event listeners to dynamically created elements
    attachTodoEventListeners();

    // Animate cards in
    animateCardsIn();
}

function createTodoCard(todo) {
    const createdDate = new Date(todo.created_at).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });

    return `
        <div class="todo-card status-${todo.status}" data-id="${todo.id}">
            <div class="todo-card-header">
                <h3 class="todo-title">${escapeHtml(todo.title)}</h3>
                <div class="todo-actions">
                    <button class="btn-icon btn-delete" data-id="${todo.id}" title="Delete task">
                        <i class="fas fa-trash"></i>
                    </button>
                </div>
            </div>
            ${todo.description ? `<p class="todo-description">${escapeHtml(todo.description)}</p>` : ''}
            <div class="todo-meta">
                <select class="status-select" data-id="${todo.id}">
                    <option value="pending" ${todo.status === 'pending' ? 'selected' : ''}>Pending</option>
                    <option value="in_progress" ${todo.status === 'in_progress' ? 'selected' : ''}>In Progress</option>
                    <option value="completed" ${todo.status === 'completed' ? 'selected' : ''}>Completed</option>
                </select>
                <span class="todo-timestamp">${createdDate}</span>
            </div>
        </div>
    `;
}

function attachTodoEventListeners() {
    // Status change listeners
    document.querySelectorAll('.status-select').forEach(select => {
        select.addEventListener('change', (e) => {
            const id = parseInt(e.target.dataset.id);
            const newStatus = e.target.value;
            handleStatusChange(id, newStatus);
        });
    });

    // Delete button listeners
    document.querySelectorAll('.btn-delete').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const id = parseInt(e.target.closest('.btn-delete').dataset.id);
            handleDelete(id);
        });
    });
}

function animateCardsIn() {
    const cards = document.querySelectorAll('.todo-card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        setTimeout(() => {
            card.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 50);
    });
}

// Filter Functions
function setActiveFilter(filter) {
    currentFilter = filter;

    // Update active tab
    filterTabs.forEach(tab => {
        if (tab.dataset.filter === filter) {
            tab.classList.add('active');
            tab.setAttribute('aria-selected', 'true');
        } else {
            tab.classList.remove('active');
            tab.setAttribute('aria-selected', 'false');
        }
    });

    renderTodos();
}

function getFilteredTodos() {
    if (currentFilter === 'all') {
        return todos;
    }
    return todos.filter(todo => todo.status === currentFilter);
}

function updateCounts() {
    const counts = {
        all: todos.length,
        pending: todos.filter(t => t.status === 'pending').length,
        in_progress: todos.filter(t => t.status === 'in_progress').length,
        completed: todos.filter(t => t.status === 'completed').length,
    };

    filterTabs.forEach(tab => {
        const filter = tab.dataset.filter;
        const countSpan = tab.querySelector('.count');
        if (countSpan) {
            countSpan.textContent = counts[filter] || 0;
        }
    });
}

// UI State Functions
function showLoading() {
    if (loadingState) loadingState.style.display = 'block';
    if (todosGrid) todosGrid.style.display = 'none';
    if (emptyState) emptyState.style.display = 'none';
}

function hideLoading() {
    if (loadingState) loadingState.style.display = 'none';
    if (todosGrid) todosGrid.style.display = 'grid';
}

function showEmptyState() {
    if (todosGrid) todosGrid.style.display = 'none';
    if (emptyState) emptyState.style.display = 'block';
}

function hideEmptyState() {
    if (emptyState) emptyState.style.display = 'none';
    if (todosGrid) todosGrid.style.display = 'grid';
}

// Toast Notifications
function showToast(message, type = 'success') {
    toast.textContent = message;
    toast.className = `toast ${type}`;

    // Trigger reflow for animation
    toast.offsetHeight;

    toast.classList.add('show');

    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// Utility Functions
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Export for testing
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        fetchTodos,
        createTodo,
        updateTodo,
        deleteTodo,
    };
}
