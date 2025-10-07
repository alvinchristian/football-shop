function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    const toastIcon = document.getElementById('toast-icon');
    
    if (!toastComponent) return;

    // Remove all type classes first
    toastComponent.classList.remove(
        'bg-red-50', 'border-red-200', 'bg-green-50', 'border-green-200',
        'bg-blue-50', 'border-blue-200', 'bg-white', 'border-gray-100'
    );

    // Set type styles and icon
    if (type === 'success') {
        toastComponent.classList.add('bg-gradient-to-br', 'from-green-50', 'to-emerald-50', 'border-green-200');
        toastComponent.style.border = '1px solid rgb(187 247 208)';
        toastIcon.textContent = '✓';
        toastIcon.className = 'text-3xl flex-shrink-0 w-10 h-10 rounded-full bg-green-500 text-white flex items-center justify-center font-bold';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-gradient-to-br', 'from-red-50', 'to-rose-50', 'border-red-200');
        toastComponent.style.border = '1px solid rgb(254 202 202)';
        toastIcon.textContent = '✕';
        toastIcon.className = 'text-3xl flex-shrink-0 w-10 h-10 rounded-full bg-red-500 text-white flex items-center justify-center font-bold';
    } else {
        toastComponent.classList.add('bg-white', 'border-gray-100');
        toastComponent.style.border = '1px solid rgb(243 244 246)';
        toastIcon.textContent = 'ℹ';
        toastIcon.className = 'text-3xl flex-shrink-0 w-10 h-10 rounded-full bg-blue-500 text-white flex items-center justify-center font-bold';
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}