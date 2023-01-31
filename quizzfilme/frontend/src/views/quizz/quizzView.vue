<template>
    <div>
        <p> Qual seu horário favorito?</p>
        <v-radio-group v-model="horario">
            <v-radio label="Manhã" value="a"></v-radio>
            <v-radio label="Tarde" value="b"></v-radio>
            <v-radio label="Noite" value="c"></v-radio>
            <div>{{ horario }}</div>
        </v-radio-group>

        <p> Qual sua planta favorita?</p>
        <v-radio-group v-model="planta">
            <v-radio label="Margarida" value="a"></v-radio>
            <v-radio label="Samambaia" value="b"></v-radio>
            <v-radio label="Beladona" value="c"></v-radio>
            <div>{{ planta }}</div>
        </v-radio-group>

        <p> Qual sua bebida favorita?</p>
        <v-radio-group v-model="bebida">
            <v-radio label="chá" value="a"></v-radio>
            <v-radio label="suco" value="b"></v-radio>
            <v-radio label="Café" value="c"></v-radio>
            <div>{{ bebida }}</div>
        </v-radio-group>
        <v-btn @click="contabilizarRespostas()">
            Submit
        </v-btn>
    </div>
</template>
  
<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"
import tratamentoQuizz from "@/helpers/tratamentoQuizz.js"
import resultadoApi from "@/api/resultado.api.js"

export default {
data () {
    return {
    horario: '',
    planta: '',
    bebida: '',
    }
},
computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
},
methods: {
    contabilizarRespostas(){
        let respostas = []
        respostas.push(this.horario, this.planta, this.bebida)
        console.log(respostas)
        let result = tratamentoQuizz.defineLetra(respostas)
        this.salvarResultado(result)
        return result
    },
    salvarResultado(resultado){
        this.loading = true
      resultadoApi.addNewResultado(resultado).then((resultado) => {
        this.loading = false
        this.$router.push({ name: "resultado" })
        console.log(resultado)
      }) .catch((error) => {
            console.log('ferrou')
            this.loading = false
        })

    }
},
}
</script>
