
// const tapBox = document.getElementById('drop-doun')
// const hiddenBox = document.getElementById('hidden_box')
// const imgStrelka = document.getElementById('img-strelka')



document.addEventListener('click', e => { // Слушаем весь документ на предмет изменения цены или колличества
    if (e.target.matches('span[class="interface drop-doun"]')) { // Если событие произошло на input ...
        let id = e.target.id.slice(10) // Отделяем id либо от цены либо от количества
        dropDoun('interface', id)
    } 
    if (e.target.matches('span[class="equipment drop-doun"]')) { // Если событие произошло на input ...
        let id = e.target.id.slice(10) // Отделяем id либо от цены либо от количества
        dropDoun('equipment', id)
    } 
    if (e.target.matches('span[class="room drop-doun"]')) { // Если событие произошло на input ...
        let id = e.target.id.slice(10) // Отделяем id либо от цены либо от количества
        dropDoun('room', id)
    } 
    // if (e.target.matches('input[class="listWorkElement"]')) { // Если событие произошло на input ...
        // let id = e.target.id.slice(10) // Отделяем id либо от цены либо от количества
        // summElements('work', id)
        // summAllElemrnts()
    // }
    
  });

  function dropDoun(mark, id) { // Открывает закрывает Div
    const hiddenBox = document.getElementById('hidden-box-'+mark+'-'+id)
    const imgStrelka = document.getElementById('img-strelka-'+mark+'-'+id)
    
    if (hiddenBox.classList.contains('not-visible')){ // Если у resultsBoxWork (блок div) есть класс 'not-visible'
        hiddenBox.classList.remove('not-visible') // Удаляем его нахрен (становится видимым)
        imgStrelka.classList.add('strelka-rotate')
    }
    else{
        hiddenBox.classList.add('not-visible')
        imgStrelka.classList.remove('strelka-rotate')
    }
}