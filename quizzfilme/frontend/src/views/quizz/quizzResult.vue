<template>
  <div>
  <v-card
    class="mx-auto mt-10"
    max-width="900"
  >
    <v-img
      class="align-end text-white"
      height="200"
      src="@/assets/background-home.png"
      cover
    >
      <v-card-title color="deep-purple-darken-4">{{infos.personalidade}}</v-card-title>
    </v-img>
    <v-card-text>
      <div>Baseado nas respostas do seu Quizz</div>

      <div>Pesquisamos o filme que mais combina com você!</div>
    </v-card-text>

    <v-card-actions>
      <v-btn color="deep-purple-darken-4">
        Share
      </v-btn>

      <v-btn color="deep-purple-darken-4" @click="showfilmes()">
        Ver filmes
      </v-btn>
    </v-card-actions>
    <v-card
    elevation="10"
    outlined
    v-if="show"
    class="pa-3"
  >  
  <v-row no-gutters>
      <v-col
        cols="12"
        sm="4"
      >
        <v-img
        max-height="225"
        max-width="303"
        :src="posterImg"
      ></v-img>
        
      </v-col>

      <v-col
        cols="12"
        sm=""
      >
    
        <p class="ma-2"> {{ this.infos.titulo }}</p>
        <p class="ma-2"> {{ this.infos.resumo }}</p>
        <v-rating 
          v-model="rating" 
          @update:modelValue="rate"
          clearable
        ></v-rating>
        
      </v-col>
    </v-row>
  </v-card>
  </v-card>

</div>
  
</template>
  
<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"
import resultadoApi from "@/api/resultado.api"

export default {
data () {
    return {
    posterImg: '',
    infos: '',
    show: false,
    resultado: '',
    length: 3,
    window: 0,
    }
},
computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
},
mounted() {
    this.getResultado()
  },
  methods: {
    rate (rating, post_id) {
      fetch(`/rate/${post_id}/${rating}/`, {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json'
              }
            }).then(rest => {
                window.location.reload();
            })
    },
    getResultado() {
      this.loading = true
      resultadoApi.getResultado().then((data) => {
        this.infos = data
        this.posterImg = `https://image.tmdb.org/t/p/original/${this.infos.poster_path}`
        console.log(posterImg)
        this.loading = false
      })
    },
    showfilmes(){
      if (this.show === true){
        this.show = false
      }else{
        this.show=true
      }
    }
    }
}
</script>
