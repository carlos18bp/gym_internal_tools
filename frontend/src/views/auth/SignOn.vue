<template>
  <div class="absolute">
    <div class="flex justify-center p-4">
      <img src="@/assets/images/logo/logo1.png">
    </div>
  </div>
  <section class="pt-16 flex h-screen items-center md:pt-0">
    <form class="space-y-5 px-8 w-full md:px-32 2xl:px-72 xl:w-1/2 2xl:w-2/3 order-2">
      <h1 class="font-bold text-center text-2xl xl:text-3xl 2xl:text-4xl">
        Te damos la bienvenida
      </h1>
      <div>
        <label for="email" class="block mb-2 text-sm font-medium text-gray-900">
          Correo electronico
        </label>
        <input
          v-model="userForm.email"
          type="email"
          id="email"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
          required
        />
      </div>

      <div>
        <label
          for="password"
          class="block mb-2 text-sm font-medium text-gray-900"
        >
          Contraseña
        </label>
        <input
          v-model="userForm.password"
          type="password"
          id="password"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
        />
      </div>

      <div>
        <label
          for="confirm_password"
          class="block mb-2 text-sm font-medium text-gray-900"
        >
          Confirmar contraseña
        </label>
        <input
          v-model="userForm.confirmPassword"
          type="password"
          id="confirm_password"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
        />
      </div>

      <div class="grid md:grid-cols-2 md:gap-6">
        <div>
          <label
            for="first_name"
            class="block mb-2 text-sm font-medium text-gray-900"
          >
            Nombre
          </label>
          <input
            v-model="userForm.firstName"
            type="text"
            id="first_name"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
          />
        </div>
        <div>
          <label
            for="last_name"
            class="block mb-2 text-sm font-medium text-gray-900"
          >
            Apellido
          </label>
          <input
            v-model="userForm.lastName"
            type="text"
            id="last_name"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
          />
        </div>
      </div>

      <button
        @click.prevent="sendVerificationPasscode"
        type="submit"
        class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full px-5 py-2.5 text-center"
      >
        Registrarse
      </button>

      <div v-if="passcodeSent" class="flex gap-4">
        <input
          v-model="passcode"
          type="text"
          id="passcode"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
          placeholder="Copy your code sent"
        />
        <button
          @click.prevent="signOnUser"
          type="submit"
          class="text-white bg-blue-500 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full px-5 py-2.5 text-center"
        >
          Código de verificación
        </button>
      </div>

      <div class="flex flex-col">
        <p class="font-regular">
          ¿Tienes una cuenta?
          <a class="font-regular text-blue-800">
            <RouterLink :to="{ name: 'sign_in' }"> Iniciar sesión </RouterLink>
          </a>
        </p>
        <div class="flex items-center w-full max-w-lg mt-4">
          <div class="flex-grow border-t border-gray-300"></div>
          <span class="mx-4 text-gray-500">O continuar con</span>
          <div class="flex-grow border-t border-gray-300"></div>
        </div>
        <div class="flex justify-center">
          <GoogleLogin class="mt-6" :callback="handleLoginWithGoogle" prompt />
        </div>
      </div>
    </form>
    <div class="h-screen hidden overflow-hidden order-1 xl:w-1/2 2xl:w-1/3 xl:block">
      <img
        src="@/assets/images/signIn/signIn.jpg"
        alt="illustration"
        class="w-full h-full object-cover"
      />
    </div>
  </section>
</template>

<script setup>
import axios from "axios";
import router from "@/router";
import { onMounted, reactive, ref } from "vue";
import { useAuthStore } from "@/stores/auth";
import { loginWithGoogle } from "@/shared/login_with_google";
import { showNotification } from "@/shared/notification_message";

const authStore = useAuthStore(); // Get the authentication store instance

const userForm = reactive({
  email: "",
  firstName: "",
  lastName: "",
  password: "",
  confirmPassword: "",
});

const passcode = ref("");
const passcodeSent = ref("");
const emailUsedToSentPasscode = ref("");

onMounted(() => {
  if (authStore.isAuthenticated) {
    router.push({
      name: "process_list",
      params: {
        user_id: userId,
        display: "",
      },
    }); // Redirect to process_list if already authenticated
  }
});

/**
 * Sends a verification passcode to the user's email.
 *
 * This function performs the following steps:
 * 1. Validates the input fields using the `checkInputs` function.
 * 2. Displays a notification indicating that an access code has been sent.
 * 3. Attempts to send a verification code to the provided email address via an API request.
 * 4. If successful, stores the passcode in the `passcodeSent` reactive variable.
 * 5. If the email is already registered (status code 409), displays an appropriate notification.
 * 6. Handles other errors by displaying a generic error notification.
 *
 * @async
 * @function sendVerificationPasscode
 * @throws Will display an error notification if the API request fails for any reason.
 */
const sendVerificationPasscode = async () => {
  checkInputs();
  showNotification("An access code has been sent to your email", "info");
  try {
    emailUsedToSentPasscode.value = userForm.email;
    const response = await axios.post("/api/sign_on/send_verification_code/", {
      email: userForm.email,
    });

    passcodeSent.value = response.data.passcode;
  } catch (error) {
    console.error("Error during verification code process:", error);
    if (error.response && error.response.status === 409) {
      showNotification("The email is already registered", "error");
    } else {
      showNotification("Send code failed!", "error");
    }
  }
};

/**
 * Handles user sign on process
 */
const signOnUser = async () => {
  checkInputs();
  if (emailUsedToSentPasscode.value !== userForm.email) {
    showNotification(
      "You have changed the verification email, you will have to generate a new code again",
      "warning"
    );
    return;
  }

  if (passcodeSent.value == passcode.value) {
    const response = await axios.post("/api/sign_on/", {
      email: emailUsedToSentPasscode.value,
      password: userForm.password,
      first_name: userForm.firstName,
      last_name: userForm.lastName,
      passcode: passcode.value,
    });
    authStore.login(response.data); // Log in the user

    showNotification("Sign On successful!", "success");
    router.push({
      name: "process_list",
      params: {
        user_id: userId,
        display: "",
      },
    }); // Redirect to process_list
  } else {
    showNotification("Code is not valid", "warning");
  }
  try {
  } catch (error) {
    console.error("Error during sign on process:", error);
    showNotification("Sign On failed!", "error");
  }
};

/**
 * Check input fields to avoid empty data
 */
const checkInputs = () => {
  if (!userForm.email) {
    showNotification("Email is required", "warning");
    return;
  }
  if (!userForm.password) {
    showNotification("Passwords is required", "warning");
    return;
  }
  if (!userForm.confirmPassword) {
    showNotification("Confirm Passwords is required", "warning");
    return;
  }
  if (userForm.password !== userForm.confirmPassword) {
    showNotification("Passwords do not match!", "warning");
    return;
  }
  if (userForm.password !== userForm.confirmPassword) {
    showNotification("Passwords do not match!", "warning");
    return;
  }
};

/**
 * Handles login with Google response
 */
const handleLoginWithGoogle = (response) => {
  loginWithGoogle(response, router, authStore);
};
</script>
