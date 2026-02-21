<template>
  <div class="page">
    <header class="hero">
      <div class="hero__content">
        <p class="eyebrow">DICOM De-Identification</p>
        <h1>Strip personal identifiers from DICOM files.</h1>
        <p class="subhead">
          Upload single files or series. We blank personal-info tags and return a
          file with the same name.
        </p>
        <div class="hero__badges">
          <span class="badge">No database storage</span>
          <span class="badge">2D + 3D series</span>
          <span class="badge">Lightweight</span>
        </div>
      </div>
      <div class="hero__panel">
        <div class="panel">
          <div class="panel__header">
            <div class="panel__dot"></div>
            <div class="panel__dot"></div>
            <div class="panel__dot"></div>
            <span>Upload</span>
          </div>
          <div class="panel__body">
            <label class="upload">
              <input type="file" multiple @change="onFileChange" />
              <span class="upload__title">Choose DICOM file(s)</span>
              <span class="upload__hint">Drag and drop or click to browse</span>
            </label>
            <button class="primary" type="button" :disabled="!canSubmit" @click="submit">
              {{ isLoading ? "Processing..." : "De-identify and download" }}
            </button>
            <p class="note" v-if="error">{{ error }}</p>
            <p class="note" v-else-if="files.length">
              {{ files.length }} file(s) selected
            </p>
            <p class="note" v-else>
              Files are processed in memory. No database storage.
            </p>
          </div>
        </div>
      </div>
    </header>

    <section class="details">
      <div class="detail">
        <h3>What we remove</h3>
        <p>
          Personal information tags only. The output file name stays the same as
          the input.
        </p>
      </div>
      <div class="detail">
        <h3>How it works</h3>
        <p>
          Files are processed in memory when possible and never stored in a
          database.
        </p>
      </div>
      <div class="detail">
        <h3>Coming later</h3>
        <p>
          Custom tag selection, optional redaction workflows, and audit-friendly
          reporting.
        </p>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed, ref } from "vue";

const files = ref([]);
const isLoading = ref(false);
const error = ref("");

const canSubmit = computed(() => files.value.length > 0 && !isLoading.value);

function onFileChange(event) {
  error.value = "";
  files.value = Array.from(event.target.files || []);
}

async function submit() {
  if (!files.value.length) return;

  isLoading.value = true;
  error.value = "";

  const formData = new FormData();
  files.value.forEach((file) => formData.append("files", file));

  try {
    const apiBase = import.meta.env.VITE_API_BASE || "";
    const response = await fetch(`${apiBase}/api/deidentify`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const message = await response.json().catch(() => ({ error: "Upload failed" }));
      throw new Error(message.error || "Upload failed");
    }

    const disposition = response.headers.get("content-disposition") || "";
    const filenameMatch = disposition.match(/filename="?([^";]+)"?/i);
    const filename = filenameMatch ? filenameMatch[1] : "deidentified.zip";

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(url);
  } catch (err) {
    error.value = err.message || "Something went wrong";
  } finally {
    isLoading.value = false;
  }
}
</script>
