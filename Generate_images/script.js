function generateGraph() {
    var diningName = document.getElementById('diningName').value;
    var container_waste = document.getElementById('container_waste');
    var container_highest = document.getElementById('container_highest');
    
    if (diningName == 'Globe') {
        graphImage_waste.src = 'food_wastage_per_week_Globe.png';
        graphImage_highest.src = 'highest_selling_food_per_week_Globe.png';
        container_highest.classList.remove('hidden');
        container_waste.classList.remove('hidden');
    }else if(diningName = 'Chipotle'){
        graphImage_waste.src = 'food_wastage_per_week_Chipotle.png';
        graphImage_highest.src = 'highest_selling_food_per_week_Chipotle.png';
        container_highest.classList.remove('hidden');
        container_waste.classList.remove('hidden');
    }
     else {
        alert('Please enter a dining name');
        // Optionally, you can add the hidden class back to the containers if the input is empty
        container_highest.classList.add('hidden');
        container_waste.classList.add('hidden');
    }
}
