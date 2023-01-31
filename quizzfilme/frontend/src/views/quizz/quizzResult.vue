<template>

</template>
  
<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"

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
 
},
}
</script>
