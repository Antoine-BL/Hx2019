<template>
<div class="container center-container">
 <b-form @submit="onSubmit" class="jumbotron w-100">

   <b-form-group id="emailGroup"
                 label="Adresse courriel:"
                 label-for="tbCourriel">
     <b-form-input id="tbCourriel"
                   type="email"
                   v-model="form.email"
                   required
                   placeholder="Saisissez votre courriel">
     </b-form-input>
   </b-form-group>
   <b-form-group id="nameGroup"
                 label="Votre nom:"
                 label-for="tbNom">
     <b-form-input  id="tbNom"
                    type="text"
                    v-model="form.name"
                    required
                    placeholder="Saisissez votre nom"
                    >
     </b-form-input>
   </b-form-group>
   <b-form-group id="password"
                 label="Votre mot de passe:"
                 label-for="tbNom">
     <b-form-input  id="tbNom"
                    type="password"
                    v-model="form.password"
                    required
                    placeholder="Saisissez votre mot de passe">
     </b-form-input>
   </b-form-group>
   <b-button type="submit" variant="primary">Soumettre</b-button>
   <b-button to="/" variant="danger">Annuler</b-button>
 </b-form>
</div>
</template>

<script>
  export default {
    data() {
      return {
        form: {
          email: '',
          name: '',
          password: '',
        }
      }
    },
    methods: {
      onSubmit (event) {
        event.preventDefault();
        alert(JSON.stringify(this.form))
      },
    }
  }
</script>

<style scoped>
.center-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 95vh;
  max-width: 500px;
}

.container > div {
  width: 100%;
}
</style>
