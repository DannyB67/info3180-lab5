<template>
    <div class="container">
        <h1>Add a New Movie</h1>
        <form @submit.prevent="saveMovie" id="movieForm" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="title" class="form-label">Title</label>
                <input type="text" class="form-control" id="title" name="title" v-model="title" required>
            </div>
            <div class="mb-3">
                <label for="description" class="form-label">Description</label>
                <textarea class="form-control" id="description" name="description" v-model="description" rows="3" required></textarea>
            </div>
            <div class="mb-3">
                <label for="poster" class="form-label">Poster Image</label>
                <input type="file" class="form-control" id="poster" name="poster" @change="handleFileUpload" required>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>

</template>

<script setup>
import { ref, onMounted } from "vue";
onMounted(() => { 
getCsrfToken(); 
}); 
let csrf_token = ref(""); 
const title = ref("");
const description = ref("");    
const posterFile = ref(null);


function getCsrfToken() { 
fetch('/api/v1/csrf-token') 
.then((response) => response.json()) 
.then((data) => { 
console.log(data); 
csrf_token.value = data.csrf_token; 
}) 
}

function saveMovie() {
let movieForm = document.getElementById('movieForm'); 
let form_data = new FormData(movieForm); 
        fetch("/api/v1/movies", {
            method: "POST",
            body: form_data,
            headers: {
                "X-CSRFToken": csrf_token.value 
            }
        })
        .then(function(response) {
            if (!response.ok) {
                return response.text().then(text => {
            throw new Error(text || "Request failed");
        });
            }
            return response.json();
        })
        .then(function (data) {
            console.log("Movie created successfully:", data);
            // Optionally, reset the form fields here
            title.value = "";
            description.value = "";
            posterFile.value = null;
        })
        .catch (function(error) {
            console.error("Error submitting form:", error);
        });
}
</script>