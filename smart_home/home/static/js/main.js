
const tapBox = document.getElementById('drop-doun')
const hiddenBox = document.getElementById('hidden_box')
const imgStrelka = document.getElementById('img-strelka')


tapBox.addEventListener('click', e => {
    if (hiddenBox.classList.contains('not-visible')){ // Если у resultsBoxWork (блок div) есть класс 'not-visible'
        hiddenBox.classList.remove('not-visible') // Удаляем его нахрен (становится видимым)
        imgStrelka.classList.add('strelka-rotate')
    }
    else{
        hiddenBox.classList.add('not-visible')
        imgStrelka.classList.remove('strelka-rotate')
    }
})