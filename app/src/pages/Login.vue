<template>
<div class="container center-container">
  <b-form class="jumbotron w-100">
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
    <b-form-group id="passwordGroup"
                  label="Mot de passe:"
                  label-for="tbPass">
      <b-form-input id="tbPass"
                    type="password"
                    v-model="form.password"
                    required
                    placeholder="Saisissez votre mot de passe">
      </b-form-input>
    </b-form-group>
    <small class="form-text text-muted">
      Besoin d'un compte?
      <router-link class="text-primary" tabindex="4" to="/signup" >
        Créez-en un!
      </router-link>
    </small>
    <b-button type="submit" variant="primary mt-3">Soumettre</b-button>
  </b-form>
</div>
</template>

<script>
  export default {
    name: "login",
    data() {
      return {
        form: {
          email: '',
          password: ''
        }
      }
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

  .container-center > div {
    width: 100%;
  }
</style>
