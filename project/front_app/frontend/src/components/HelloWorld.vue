<script setup>

import { ref } from 'vue'

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";



defineProps({
    title: String,
    button_text: String,
});

const count = ref(0);

</script>



<template>
  
  <section>
    
    
    <h1>{{ title }}</h1>
    
    <div class="card">
        
        <button class="btn btn-primary" type="button" @click="count++">
            {{button_text}} {{ count }}
        </button>
        
    </div>
  
  </section>
  
</template>



<style scoped>

</style>
