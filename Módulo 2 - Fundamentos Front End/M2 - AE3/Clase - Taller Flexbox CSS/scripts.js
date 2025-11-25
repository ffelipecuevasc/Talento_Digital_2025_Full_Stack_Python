const container = document.getElementById('flexContainer');
const mainAxis = document.getElementById('mainAxis');
const crossAxis = document.getElementById('crossAxis');
const infoText = document.getElementById('infoText');
const codeDisplay = document.getElementById('codeDisplay');

let state = {
    display: 'flex',
    direction: 'row',
    wrap: 'nowrap',
    alignItems: 'flex-start',
    alignContent: 'flex-start'
};

function updateCode() {
    codeDisplay.innerHTML = `
        <div><span class="property">display</span>: <span class="value">${state.display}</span>;</div>
        <div><span class="property">flex-direction</span>: <span class="value">${state.direction}</span>;</div>
        <div><span class="property">flex-wrap</span>: <span class="value">${state.wrap}</span>;</div>
        <div><span class="property">align-items</span>: <span class="value">${state.alignItems}</span>;</div>
        <div><span class="property">align-content</span>: <span class="value">${state.alignContent}</span>;</div>
      `;
}

function updateInfo() {
    let info = '';

    if (state.display === 'block') {
        info = '<strong>Display: block</strong> - Flexbox desactivado. Los elementos se comportan como bloques normales, apilándose verticalmente.';
    } else {
        let directionText = '';
        let axisText = '';

        if (state.direction.includes('row')) {
            directionText = state.direction === 'row' ? 'horizontalmente de izquierda a derecha' : 'horizontalmente de derecha a izquierda';
            axisText = 'El eje transversal es VERTICAL (↓)';
        } else {
            directionText = state.direction === 'column' ? 'verticalmente de arriba a abajo' : 'verticalmente de abajo a arriba';
            axisText = 'El eje transversal es HORIZONTAL (→)';
        }

        let wrapText = state.wrap === 'nowrap' ? 'sin salto de línea' :
            state.wrap === 'wrap' ? 'con salto de línea cuando no caben' :
                'con salto de línea invertido';

        info = `<strong>Flexbox activado:</strong> Los items se alinean ${directionText}, ${wrapText}. ${axisText}. `;
        info += `<strong>align-items:</strong> ${state.alignItems} alinea en el eje transversal. `;
        info += `<strong>align-content:</strong> ${state.alignContent} distribuye las líneas cuando hay wrap.`;
    }

    infoText.innerHTML = info;
}

function updateAxes() {
    if (state.display === 'block') {
        mainAxis.style.display = 'none';
        crossAxis.style.display = 'none';
        return;
    }

    mainAxis.style.display = 'block';
    crossAxis.style.display = 'block';

    if (state.direction.includes('row')) {
        mainAxis.textContent = state.direction === 'row' ? 'Eje principal →' : 'Eje principal ←';
        crossAxis.textContent = 'Eje transversal ↓';
    } else {
        mainAxis.textContent = state.direction === 'column' ? 'Eje principal ↓' : 'Eje principal ↑';
        crossAxis.textContent = 'Eje transversal →';
    }
}

function setDisplay(value) {
    state.display = value;

    if (value === 'flex') {
        container.style.display = 'flex';
        container.classList.remove('no-flex');
    } else {
        container.style.display = 'block';
        container.classList.add('no-flex');
    }

    updateActiveButton('display', value);
    updateCode();
    updateInfo();
    updateAxes();
}

function setDirection(value) {
    state.direction = value;
    container.style.flexDirection = value;

    updateActiveButton('direction', value);
    updateCode();
    updateInfo();
    updateAxes();
}

function setWrap(value) {
    state.wrap = value;
    container.style.flexWrap = value;

    updateActiveButton('wrap', value);
    updateCode();
    updateInfo();
}

function setAlignItems(value) {
    state.alignItems = value;
    container.style.alignItems = value;

    updateActiveButton('alignItems', value);
    updateCode();
    updateInfo();
}

function setAlignContent(value) {
    state.alignContent = value;
    container.style.alignContent = value;

    updateActiveButton('alignContent', value);
    updateCode();
    updateInfo();
}

function updateActiveButton(property, value) {
    const mapping = {
        'display': { 'flex': 'flex', 'block': 'block' },
        'direction': {
            'row': 'row',
            'row-reverse': 'row-reverse',
            'column': 'column',
            'column-reverse': 'column-reverse'
        },
        'wrap': {
            'nowrap': 'nowrap',
            'wrap': 'wrap',
            'wrap-reverse': 'wrap-reverse'
        },
        'alignItems': {
            'flex-start': 'items-start',
            'center': 'items-center',
            'flex-end': 'items-end',
            'stretch': 'items-stretch',
            'baseline': 'items-baseline'
        },
        'alignContent': {
            'flex-start': 'content-start',
            'center': 'content-center',
            'flex-end': 'content-end',
            'stretch': 'content-stretch',
            'space-between': 'content-between',
            'space-around': 'content-around',
            'space-evenly': 'content-evenly'
        }
    };

    const buttons = mapping[property];
    Object.values(buttons).forEach(btnId => {
        const btn = document.getElementById('btn-' + btnId);
        if (btn) btn.classList.remove('active');
    });

    const activeBtn = document.getElementById('btn-' + buttons[value]);
    if (activeBtn) activeBtn.classList.add('active');
}

// Inicializar
updateCode();
updateInfo();
updateAxes();